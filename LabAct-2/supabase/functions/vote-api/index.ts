import { serve } from "https://deno.land/std@0.168.0/http/server.ts"
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'

serve(async (req) => {
  try {
    const supabase = createClient(
      Deno.env.get('SUPABASE_URL') ?? '',
      Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? ''
    )

    const { user_id, poll_id, choice, node_id } = await req.json()

    const { error } = await supabase
      .from('vote_queue')
      .insert([
        { 
          payload: { user_id, poll_id, choice, node_id },
          status: 'pending' 
        }
      ])

    if (error) throw error

    return new Response(JSON.stringify({ message: "Vote Queued" }), {
      headers: { "Content-Type": "application/json" },
      status: 202,
    })

  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      headers: { "Content-Type": "application/json" },
      status: 400,
    })
  }
})